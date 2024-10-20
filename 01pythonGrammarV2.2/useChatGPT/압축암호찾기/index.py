import zipfile
import itertools

def crack_zip(zip_file, password):
    try:
        # zip 파일 열기
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            # 암호 시도
            zip_ref.extractall(pwd=password.encode())
            print(f"암호 '{password}'로 성공적으로 압축을 해제했습니다.")
            return True
    except Exception as e:
        # 암호가 틀렸을 경우
        #print(e)  # 디버깅용
        return False

def main():
    #zip_file = input("암호를 찾을 zip 파일의 경로를 입력하세요: ")
    zip_file = './saveFiles/slamDunk.zip'
    
    # 가능한 암호 조합 생성 및 시도
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for length in range(1, 10):  # 1자리부터 9자리까지 시도
        for password in itertools.product(characters, repeat=length):
            password = ''.join(password)
            print(f"시도 중인 암호: {password}")
            if crack_zip(zip_file, password):
                return

    print("암호를 찾지 못했습니다.")

if __name__ == "__main__":
    main()
