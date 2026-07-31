import torch
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from fastsam import FastSAM, FastSAMPrompt


def get_device():
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("CUDA is available. Using GPU.")
    # Check for MPS (Apple Silicon)
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
        print("MPS is available. Using Apple GPU.")
    # Default to CPU
    else:
        device = torch.device("cpu")
        print("Using CPU.")
    return device

def resize_image(image, input_size=1024):
    w, h = image.size
    scale = input_size / max(w, h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    image = image.resize((new_w, new_h))
    return image

def get_raw_image(path_to_img):
    raw_image = Image.open(path_to_img)
    return raw_image

def get_results(resized_image, model, device, retina_masks=True, imgsz=1024, conf=0.6, iou=0.9):
    """
    I have 'FastSAM-s.pt' and 'FastSAM.pt' on my laptop.
    """
    model = FastSAM(model)  # or another FastSAM checkpoint
    results = model(resized_image, device=device, retina_masks=retina_masks,
                    imgsz=imgsz, conf=conf, iou=iou)#[0] messes casia env up
    return results


def plot_grid(resized_image, results_objects, overlay_function, titles=None, n_cols=3, alpha=0.75, **kwargs):
    """
    Shows grid of result masks
    """
    n_images = len(results_objects)
    
    # Validation check: Ensure titles are provided and match the number of result objects
    if isinstance(titles,str): titles = [titles]
    if titles and len(titles) != n_images:
        raise ValueError("The number of titles must match the number of result objects.")

    n_rows = (n_images + n_cols - 1) // n_cols  # Calculate the number of rows needed
    
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(n_cols * 4, n_rows * 4))
    axs = axs.flatten()  # Flatten in case of multi-row subplots
    
    for idx, obj in enumerate(results_objects):
        plt.sca(axs[idx])  # Set the current axes to the subplot
        overlay_function(resized_image, obj, alpha=alpha, ax=axs[idx], **kwargs)  # Use the provided function
        axs[idx].axis('off')  # Optional: turn off axis labels
        if titles:
            axs[idx].set_title(titles[idx], fontsize=10)
    
    # If there are more subplots than images, hide the unused subplots
    for idx in range(n_images, n_rows * n_cols):
        axs[idx].axis('off')

    plt.tight_layout()
    plt.show()



def bounding_box_overlay(resized_image, results_objects, linewidth=2, edgecolor='orange', 
                      alpha=1.0, first_box_color=None, first_box_line=None, ax=None):
    if first_box_color is None: first_box_color = edgecolor
    color_map = {0:first_box_color}
    if first_box_line is None: first_box_line = linewidth
    line_map = {0:first_box_line}
    if ax is None:
        fig, ax = plt.subplots(1)
    ax.imshow(resized_image)
    for idx,obj in enumerate(results_objects):
        color = color_map.get(idx,edgecolor)
        lwidth = line_map.get(idx,linewidth)
        x1, y1, x2, y2 = obj.summary()[0]['box'].values()
        w = x2-x1
        h = y2-y1
        # Create a Rectangle patch
        rect = patches.Rectangle((x1, y1), w, h, linewidth=lwidth, edgecolor=color, 
                                 facecolor='none', alpha=alpha)
        ax.add_patch(rect)

def bounding_box_grid(resized_image, results_objects, titles=None, n_cols=3, **kwargs):
    plot_grid(resized_image, results_objects, bounding_box_overlay, titles=titles, n_cols=n_cols, **kwargs)

def segmentation_contour_overlay(resized_image, results_objects, 
        first_obj_edge='red', first_obj_face='orange', first_obj_line=3, alpha=0.5, ax=None):
    edge_map = {0:first_obj_edge}
    face_map = {0:first_obj_face}
    line_map = {0:first_obj_line}
    if ax is None:
        fig, ax = plt.subplots(1)
    ax.imshow(resized_image)
    for idx,obj in enumerate(results_objects):
        edgecolor = edge_map.get(idx,'blue')
        facecolor = face_map.get(idx,'yellow')
        linewidth = line_map.get(idx,2)
        xy = obj.masks.xy[0]
        # Create a Polygon patch
        polygon = patches.Polygon(xy, closed=True, linewidth=linewidth, 
                        edgecolor=edgecolor, facecolor=facecolor, alpha=alpha)
        ax.add_patch(polygon)

def segmentation_contour_grid(resized_image, results_objects, titles=None, n_cols=3, alpha=0.5, **kwargs):
    plot_grid(resized_image, results_objects, segmentation_contour_overlay, 
              titles=titles, n_cols=n_cols, alpha=alpha, **kwargs)


def get_prompt_results(resized_image, model, prompts, device=None):
    # FastSAM Results 
    model_results = get_results(resized_image, model, device=device)

    # Prompters
    prompter = FastSAMPrompt(resized_image, model_results, device=device)

    # Prompt Results
    if isinstance(prompts,str): prompts = [prompts]
    prompt_results = []
    for prompt in prompts:
        results = prompter.text_prompt(text=prompt)
        prompt_results.append(results)
    return prompt_results









# Ultralytics
def text_prompt(self, text, clip_download_root=None):
    """Processes a text prompt, applies it to existing results and returns the updated results."""
    if self.results[0].masks is not None:
        format_results = self._format_results(self.results[0], 0)
        cropped_images, filter_id, annotations = self._crop_image(format_results)
        clip_model, preprocess = self.clip.load("ViT-B/32", download_root=clip_download_root, device=self.device)
        scores = self.retrieve(clip_model, preprocess, cropped_images, text, device=self.device)
        max_idx = torch.argmax(scores)
        max_idx += sum(np.array(filter_id) <= int(max_idx))
        self.results[0].masks.data = torch.tensor(np.array([annotations[max_idx]["segmentation"]]))
    return self.results

# Casia
def text_prompt(self, text):
    if self.results == None:
        return []
    format_results = self._format_results(self.results[0], 0)
    cropped_boxes, cropped_images, not_crop, filter_id, annotations = self._crop_image(format_results)
    clip_model, preprocess = clip.load('ViT-B/32', device=self.device)
    scores = self.retrieve(clip_model, preprocess, cropped_boxes, text, device=self.device)
    max_idx = scores.argsort()
    max_idx = max_idx[-1]
    max_idx += sum(np.array(filter_id) <= int(max_idx))
    return np.array([annotations[max_idx]['segmentation']])