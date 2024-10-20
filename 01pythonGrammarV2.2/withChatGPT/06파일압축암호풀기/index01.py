import zipfile
import itertools

def find_zip_password(zip_file_path):
    with zipfile.ZipFile(zip_file_path) as zip_file:
        # 가능한 암호 생성
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        
        for length in range(1, 10):
            for password in itertools.product(characters, repeat=length):
                password = ''.join(password)
                print(password)
                
                try:
                    zip_file.extractall(pwd=password.encode('utf-8'))
                    print(f"올바른 암호: {password}")
                    return password                
                except Exception:
                    pass
        
        print("암호를 찾지 못했습니다.")
        return None

find_zip_password('./resData/secretFiles.zip')

