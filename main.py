from manager.Main import Main


config = {
    'file_name': 'src/students.txt',
}

main = Main(config['file_name'])
main.run()
