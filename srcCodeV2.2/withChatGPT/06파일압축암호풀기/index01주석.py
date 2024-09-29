'''
질문] 파이썬으로 zip 파일의 암호를 찾는 예제코드를 만들어줘. 숫자, 영문자를 입력해서 찾는 방법이야. 암호는 자리수는 1~9자리까지야. 코드에 주석을 이용해서 코드를 설명해줘. 코드는 함수로 만들어줘. 함수의 사용까지 알려줘.
'''

import zipfile
import itertools

def find_zip_password(zip_file_path):
    """
    암호 보호된 ZIP 파일의 암호를 찾는 함수.

    파라미터:
    zip_file_path (str): ZIP 파일의 경로.

    반환:
    str: 올바른 암호를 찾으면 암호를 반환하고, 찾지 못하면 None을 반환.

    사용 예:
    find_zip_password('example.zip')
    """
    # ZIP 파일 열기
    with zipfile.ZipFile(zip_file_path) as zip_file:
        # 가능한 암호 생성 (숫자와 영문자를 포함하여 1~9자리 암호 생성)
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        
        # 1~9자리까지 모든 암호 조합 테스트
        for length in range(1, 10):
            # 가능한 모든 조합
            for password in itertools.product(characters, repeat=length):
                password = ''.join(password)
                print(password)
                
                try:
                    # 주어진 암호로 ZIP 파일 열기 시도
                    zip_file.extractall(pwd=password.encode('utf-8'))
                    
                    # 암호를 찾으면 반환
                    print(f"올바른 암호: {password}")
                    return password
                
                except Exception:
                    # 암호가 틀렸을 경우 다음 암호로 넘어감
                    pass
        
        # 암호를 찾지 못했을 경우 None 반환
        print("암호를 찾지 못했습니다.")
        return None

# 함수 사용 예:
# zip_file_path에 ZIP 파일 경로를 전달하여 함수를 사용합니다.
# 예: find_zip_password('example.zip')
find_zip_password('./saveFiles/saveFiles.zip')