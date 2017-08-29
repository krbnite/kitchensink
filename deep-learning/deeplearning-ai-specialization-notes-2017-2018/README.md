# deeplearning.ai
Notes and projects associated with Andrew Ng's Deep Learning specialization on Coursera


# Good to Know
Deep Learning Honor Code

We strongly encourage students to form study groups, and discuss the lecture videos (including in-video questions). We also encourage you to get together with friends to watch the videos together as a group. However, the answers that you submit for the review questions should be your own work. For the programming exercises, you are welcome to discuss them with other students, discuss specific algorithms, properties of algorithms, etc.; we ask only that you not look at any source code written by a different student, nor show your solution code to other students.

**You are also not allowed to post your code publicly on github.**

### Adding a Private Repo to a Public Repo
Something like this could work:
* https://24ways.org/2013/keeping-parts-of-your-codebase-private-on-github/
* https://medium.com/@bilalbayasut/github-how-to-make-a-fork-of-public-repository-private-6ee8cacaf9d3
  - [StackOverflow page](https://stackoverflow.com/questions/10065526/github-how-to-make-a-fork-of-public-repository-private) w/ same content


```
# first, create a private GitHub repo, then:
git clone --bare https://github.com/krbnite/deeplearning.ai
cd public-repo.git
git push --mirror https://github.com/yourname/private.deeplearning.ai
cd ..
rm -rf public-repo.git
```

Now, whenever you want to update the private repo w/ new stuff from the public repo:
```
git clone https://github.com/krbnite/private.deeplearning.ai
cd private.deeplearning.ai
git remote add public https://github.com/krbnite/deeplearning.ai
git pull public master # Creates a merge commit
git push origin master
```

You can also push some private stuff to the public repo if you wanted to, but that's not in 
my current scope...so, \</end\>.

----------------------------------------------
