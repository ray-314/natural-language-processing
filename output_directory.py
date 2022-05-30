class Make_dir:

    def __init__(self, output_dir='test', results_dir=''):
        self.output_dir = output_dir
        self.results_dir = results_dir
        if self.results_dir == '':
            self.output_path = output_dir + '/'
        else:
            self.output_path = self.results_dir + '/' + output_dir + '/'

    def make_dir(self):
        import os
        pwd = os.getcwd()
        output_path_full = pwd + "/" + self.output_path
        if os.path.isdir(output_path_full):
            print('Set output directory : ' + self.output_path)
            print('Output full path : ' + output_path_full)
        else:
            os.mkdir(self.output_path)
            print('Make output directory : ' + self.output_path)
            print('Output full path : ' + output_path_full)
        return self.output_path