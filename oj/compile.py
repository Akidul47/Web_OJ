import subprocess
import os
import time

class CompileJava:
    def __init__(self, code, id) -> None:
        self.file_name = "code-" + str(id) + ".java"
        self.code = code
        self.retry_count = 5
    
    def to_file(self):
        try:
            with open(self.file_name, "w") as c:
                c.write(self.code)
        except Exception as e:
            return str(e)

        return True

    def compile(self):
        cmd = '/usr/bin/javac ' + self.file_name
        try:
            proc = subprocess.Popen(cmd, shell=True)
            proc.communicate()
        except Exception as e:
            out = ""
            err = "error compiling: " + str(e)    
            return out, err

        while not os.path.isfile("HelloWorld.class"):
            self.retry_count -= 1
            time.sleep(.1)
            print("retrying--- ", self.retry_count)
            if self.retry_count < 1:
                break

        run_cmd = "/usr/bin/java HelloWorld"
        try:
            proc = subprocess.Popen(run_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = proc.communicate()
        except Exception as e:
            out = ""
            err = "error java exed: " + str(e)
            return out, err

        return out.decode('utf-8'), err.decode('utf-8')
        return out, err

                
if __name__ == "__main__":

    code = """
    class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello, World!"); 
        }
    }

    """
    cj = CompileJava(code, "this")
    ret = cj.to_file()
    if not ret:
        print("error writing file: ", ret)
    out, err = cj.compile()
    print("Success: ", out)
    print("Error: ", err)