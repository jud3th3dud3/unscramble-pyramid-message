# unscramble-pyramid-message
This code will sort corresponding words and numbers from a text file, place the words into a pyramid, and return all the last words from each row in the pyramid.

To run this code:

1. Clone the repo: ```git clone <url>```

2. Navigate into the repo folder with your terminal: ```cd <repo folder path>```

Without the container:

3. Run the Python script: ```<python3 unscramble.py>```

With the container:

3. Build the Docker image: ```docker build -t unscramble-message .```

4. Run the Docker container: ```docker run --rm unscramble-message```

It will then print the output for you!

Feel free to edit the file location within the .py file to point to the document that you want to sort.