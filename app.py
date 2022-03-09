#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import speech_recognition as sr


# In[4]:


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print("File Received")
        filename = secure_filename(file.filename)
        print(filename)
        file.save("static/" + filename)
        a = sr.AudioFile("static/" + filename)
        with a as source:
            a = sr.Recognizer().record(source)
        s = sr.Recognizer().recognize_google(a)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="ready"))
    
if __name__ == "__main__":
    app.run()


# In[ ]:




