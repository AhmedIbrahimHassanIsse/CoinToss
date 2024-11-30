# Coin Toss Game

## Description:
The Coin Toss game is a generic game where you guess whether a coin flip will land on "heads" or "tails". The game keeps track of how many times you've guessed correctly or incorrectly and displays your score. You can stop the game anytime by typing "End" but you can't end without making a guess or having either more right or wrong guesses.

### How to Run the App:

#### Option 1: Using Docker (Recommended)
Docker allows you to run the Coin Toss game without needing to install Python directly. Follow these steps to use Docker:

1. **Pull the Docker Image**:
   - Open Command Prompt (CMD) and run:
     ```
     docker pull ahmedihassan/coin_toss
     ```
   - This command downloads the Docker image from Docker Hub.

2. **Run the Coin Toss Game**:
   - After downloading the image, run the game using:
     ```
     docker run -it ahmedihassan/coin_toss
     ```
   - The game will start, and you will be asked to guess if the coin flip will be "heads" or "tails".

#### Option 2: Running the App Locally Using Python
If you don't have Docker but do have Python installed, you can run the Coin Toss game directly on your computer:

1. **Make Sure Python is Installed**:
   - The app requires Python 3. You can check if Python is installed by typing:
     ```
     python --version
     ```
   - If Python is not installed, you can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. **Download the Files from GitHub**:
   - Go to the GitHub repository: [GitHub Repository Link](https://github.com/AhmedIbrahimHassanIsse/CoinToss)
   - Download the **`coin_toss.py`** file.

3. **Run the Game**:
   - Open Command Prompt and navigate to where you saved `coin_toss.py`.
   - Run the game using:
     ```
     python coin_toss.py
     ```

### URLs:
- **GitHub Repository**: [GitHub Repository Link](https://github.com/AhmedIbrahimHassanIsse/CoinToss/upload)
- **Docker Hub Image**: [Docker Hub Image Link](https://hub.docker.com/r/ahmedihassan/coin_toss)

### Summary:
- The Coin Toss game is a fun, simple guessing game where you can choose "heads" or "tails" and see how often you're right.
- You can run it using Docker for the easiest setup or run it locally using Python.
- The Docker image is hosted at Docker Hub, and the source code is available on GitHub.

### Contact:
If you have any questions or run into issues running the Coin Toss game, feel free to reach out via GitHub!


