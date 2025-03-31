# PageRank Algorithm Implementation

## Overview
This project implements a simple version of Google's PageRank algorithm using NumPy. The algorithm ranks webpages based on link structures, simulating the probability of a user randomly clicking through links on a set of webpages.

## Features
- **Adjacency Matrix Representation:** Models the web as a link matrix.
- **Transition Probability Matrix:** Handles dead-end pages to ensure fair probability distribution.
- **Damping Factor Implementation:** Simulates random surfing behavior.
- **Iterative Convergence:** Computes PageRank values through matrix multiplication.

## Installation
```sh
git clone https://github.com/akitaki79/page-rank.git
cd pagerank
pip install numpy
```

## Usage
Run the script to compute PageRank values:
```sh
python pagerank.py
```

## Example Output
```sh
PageRank: [0.342 0.152 0.258 0.248]
```

## Future Improvements
- Extend the algorithm to handle larger datasets efficiently.
- Implement sparse matrix optimizations for scalability.
- Visualize the PageRank convergence process.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues and pull requests to improve the algorithm!

