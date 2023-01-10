pipeline {
    agent any
    environment {
        LT_BUILD_NAME = "lambdatest-pipeline"
    }
    stages {

  stage('Test') {
    steps {
      sh 'sleep 5' 
      sh 'python3 lambdatest.py'
    }
  }

}
}
