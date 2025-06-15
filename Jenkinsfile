pipeline {
    agent any

    triggers {
        cron('H/2 * * * *')
    }

    parameters {
        string(name: 'MESSAGE', dafaultValue: 'Hello world!', description: 'Message to be dispalyed')}

    stages {
        stage ('Say Message') {
            steps {
                echo "Message: ${params.MESSAGE}"
            }
        }
    }
}