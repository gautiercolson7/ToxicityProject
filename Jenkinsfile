pipeline {
    agent any

    stages {
        stage('Access') {
			steps {
				git([url:'https://github.com/gautiercolson7/ToxicityProject.git', branch:'main'])
			}
		}
		stage('Build docker images') {
			steps {
				bat 'docker build -t "toxicityproject_model" ./Model'
				bat 'docker build -t "toxicityproject_back" ./Backend'
				bat 'docker build -t "toxicityproject_front" ./Frontend'
			}
		}
		stage('Remove docker images') {
			steps {
			    bat 'docker image rm toxicityproject_model'
				bat 'docker image rm toxicityproject_back'
				bat 'docker image rm toxicityproject_front'
			}
		}
		stage('Docker Compose') {
			steps {
				bat 'docker-compose up'
			}
		}
    }
}