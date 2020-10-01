'use strict';
const Generator = require('yeoman-generator');
const yosay = require('yosay');
const chalk = require('chalk');
const dateformat = require('dateformat');

module.exports = class extends Generator {

    prompting() {

        this.log(
            yosay(`Welcome to the stupendous ${chalk.red('generator-pymaketool')} generator!`)
        );

        const prompts = [
            {
                type: 'input',
                name: 'projectName',
                message: 'Your project name',
                default: this.appname
            },
            {
                type: 'input',
                name: 'projectFolder',
                message: 'Your project folder',
                default: this.appname
            },
            {
                type: 'input',
                name: 'username',
                message: 'Your Username',
                store: true
            },
            {
                type: 'input',
                name: 'email',
                message: 'Your email',
                store: true
            },
            {
                type: 'list',
                name: 'projectType',
                message: 'What type of project you want to make?',
                choices: [
                    'gcc-linux',
                    'arm-none-eabi-gcc' 
                ]
            }
        ];
        return this.prompt(prompts).then(props => {
            // To access props later use this.props.someAnswer;
            this.props = props;
        });
    };

    writing() {
        let now = new Date();
        let strDate = dateformat(now, 'yyyy/dd/mm hh:MM:ss');
        var fileTokens = {
            projectName: this.props.projectName,
            projectFolder: this.props.projectFolder,
            email: this.props.email,
            username: this.props.username,
            datetime: strDate,
            type: this.props.projectType
        };

        var files = [
            "/Makefile",
            "/makefile.mk",
            "/Makefile.py",
            "/.project",
            "/.pymakeproj/.cproject_template",
            "/.pymakeproj/.language.settings_template",
            "/app/main.c",
            "/app/app_mk.py"
        ];

        var project = this.props.projectType;

        files.forEach(file => {
            this.fs.copyTpl(
                this.templatePath(project + file),
                this.destinationPath(this.props.projectName + file),
                fileTokens
            );
        });
    };

};