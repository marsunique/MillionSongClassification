## Neural Network

This neural network is patterned after the neural network provided in the [`Welch labs neural network tutorials`](http://www.welchlabs.com/blog/2015/1/16/neural-networks-demystified-part-1-data-and-architecture).  

### Feature Selection
For this project, I used one hidden layer with 15 nodes.  The output layer was a single node.  If this setup provided unsatisfying results, I would have used a round-robin approach, changing the hidden layer size and the alpha value to find an optimal setup.  

### Input Files
Currently, the algorithm is looking at the test_data_III.csv and train_data_III.csv to train the network.  I had to iterate on the same data three times to prune the values exactly as the numpy arrays dictate.  There is no leeway in this regard.  It had to be perfect.

### Issues in Implementation
There is a critical part of the trainer method that calls the scipy.optimize method.  When the trainer runs, it attempts to call this method, but returns an error based on the internals of numpy and scipy.  I spent a non-trivial amount of time looking into the root cause of this issue, then decided that my efforts were better used elsewhere in the group project

# IMAGE OF ERROR

## To Run this code:
Run the script nnRun.py.  It will start reading in the csv files and assigning them to numpy matrices (about 16 minutes on my macbook pro at home, probably an optimization out there), and begin to train the network and backpropagate.  Unfortunately, the results you will receive will be worse than random.  Any suggestions to improve my process or method are very welcome.  dalambri@ncsu.edu
