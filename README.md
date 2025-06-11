aws-cicd-python-helloworld
demo for using CI/CD in aws with simple Python hello-word application

Startup Script
chmod +x run.sh
./run.sh Access the app in a browser at http://$YOUR-PUBLIC-EC2-IP$:5000.
How to Run the Test
pip3 install flask
python test_app.py
If using this with AWS CodeDeploy
prepare your destination EC2 with AWS CodeDeploy agent with install-codedeploy-agents.sh $YOUR_REGION