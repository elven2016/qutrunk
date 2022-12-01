pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''source /home/qudoor/env.sh
rm -rf build/
rm -rf dist/
rm -rf __pycache__/
poetry check
poetry build
wait '''
      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            sh '''source /home/qudoor/env.sh
pip3 uninstall qutrunk -y
pip3 install $WORKSPACE/dist/qutrunk*.whl
python3 -c "import qutrunk;qutrunk.run_check()" '''
          }
        }

        stage('unitest') {
          steps {
            sh '''source /home/qudoor/env.sh
pip3 --default-timeout=1688 install qiskit -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com 
cd $WORKSPACE
pytest ./qutrunk/test/ '''
          }
        }

        stage('example test') {
          steps {
            sh '''source /home/qudoor/env.sh
cd $WORKSPACE/qutrunk/example/
python3  addition.py
python3  bell_pair.py
python3  bernstein_vazirani.py
python3  decrement.py
python3  deutsch.py
python3  ghz.py
python3  grover.py
python3  increment.py
python3  openqasm_parse.py
python3  phase_kickback.py
python3  qft.py
python3  qusl_parse.py
python3  random_byte.py
'''
          }
        }

      }
    }

  }
}