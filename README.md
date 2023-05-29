
# Steganography

With this project, you can encrypt any text in your image and decrypt the message from that image. First, download all the items, and then run the executive file. But sometimes it may give an error as it runs on the C drive in the Python directory. So always try to open the code with PyCharm or VS Studio and all the image files in the same folder, and then run the code.



## Saving the file

After running the code, a window will pop up, and you will insert an image for message encryption and decryption. Remember, after encrypting a message in your image, it will ask for an image file name. And you must add the name with the ".png" extension without an inverted comma.

You can get rid of this issue if you want to save the files with the same name. Than just go to code and change the code from **save** function in 37-38 lines to this code.

Fixed your file name here. Than you will do not need to give your files name every time

Always Remember, You MUST need to add **.png** extension after your file name. For example:

```bash
    #example
    def save():
        secret.save("Hidden Image.png")
```
```bash
    def save():
        secret.save("Enter your file name: ")
```
## Change Image and Icon
You can change the image and icon and replace it whatever you want. Just remind that you can only add here either **.gif** format or **.png** format. Because python does not support build in jpg format. But you can add **.jpg** format after using **matlab** library of python.
