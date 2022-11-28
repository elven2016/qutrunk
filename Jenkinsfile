pipeline {
  agent {
    node {
      label 'ubuntu22.04'
    }

  }
  stages {
    stage('git colone source') {
      steps {
        git(url: 'https://github.com/elven2016/qutrunk.git', branch: 'main')
      }
    }

  }
}