pipeline {
    agent any
    environment {
        LT_BUILD_NAME = "lambdatest-pipeline"
    }
    stages {
  stage('Setup') {
    steps {
      sh 'wget https://downloads.lambdatest.com/tunnel/v3/linux/64bit/LT_Linux.zip'
      sh 'apt-get install -y zip unzip' 
      sh 'unzip -o LT_Linux.zip'
      sh './LT --user ${LT_USERNAME} --key ${LT_ACCESS_KEY} --tunnelName jenkins-tunnel --infoAPIPort 8000 &'
    }
  }

  stage('Test') {
    steps {
      sh 'sleep 5' 
      sh 'python3 lambdatest.py'
    }
  }

}
}
