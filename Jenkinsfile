node {
   currentBuild.result = "SUCCESS"
   stage('Printing hello world'){
       sh 'echo "Hello World"'
   }
   stage('unit test'){
       sh 'echo "unit test has started"'
   }
   stage('system test'){
       sh 'pwd'
       sh 'ls -ltrha'
       sh 'python ./idit.py'
   }
   
   stage('integration test'){
       sh 'echo "integration test has started"'
   }
}
