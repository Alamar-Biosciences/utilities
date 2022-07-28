## Utility to be run as a system service, listens for curl requests and performs updates on Galaxy server
from flask import Flask,request,json
import os
app = Flask(__name__)

@app.route('/nulisaseq_cpp')
def nulisaseq_cpp():
    t0 = os.popen("docker pull alamarbiosciences/nulisaseq_cpp_galaxy").read()
    t1 = os.popen("docker pull alamarbiosciences/nulisaseq_cpp").read()
    t2 = os.popen("cd /galaxy/github/NULISAseq_cpp && git pull").read()
    return '%s\n\n%s\n\n%s\n\nDone' %(t0, t1, t2)

@app.route('/nulisaseq_cpp_galaxy')
def nulisaseq_cpp_galaxy():
    t0 = os.popen("docker pull alamarbiosciences/nulisaseq_cpp_galaxy").read()
    t1 = os.popen("docker pull alamarbiosciences/nulisaseq_cpp").read()
    t2 = os.popen("cd /galaxy/github/NULISAseq_cpp && git pull").read()
    return '%s\n\n%s\n\n%s\n\nDone' %(t0, t1, t2)

@app.route('/nulisa_cpp')
def nulisa_cpp():
    t0 = os.popen("docker pull alamarbiosciences/nulisa_cpp").read()
    t1 = os.popen("cd /galaxy/github/NULISA_cpp && git pull").read()
    return '%s\n\n%s\n\nDone' %(t0, t1)

@app.route('/nulisa')
def nulisa():
    t0 = os.popen("docker pull alamarbiosciences/nulisa").read()
    t1 = os.popen("cd /galaxy/github/NULISA && git pull").read()
    return '%s\n\n%s\n\nDone' %(t0, t1)

@app.route('/attobodyseq')
def attobodyseq():
    t0 = os.popen("docker pull alamarbiosciences/attobodyseq").read()
    t1 = os.popen("cd /galaxy/github/AttobodySeq && git pull").read()
    return '%s\n\n%s\n\nDone' %(t0, t1)

@app.route('/signaltuning')
def signaltuning():
    t0 = os.popen("docker pull alamarbiosciences/signaltuning").read()
    t1 = os.popen("cd /galaxy/github/Signal-Tuning && git pull").read()
    return '%s\n\n%s\n\nDone' %(t0, t1)
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
