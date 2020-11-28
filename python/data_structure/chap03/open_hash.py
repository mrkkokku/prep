# 오픈 주소방법으로 해시 함수 구현하기
# open addressing 방법

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0 # 데이터를 저장했다는 flag
    EMPTY = 1    # 비어있음 flag
    DELETED = 2  # 삭제완료 flag

class Bucket:
    ''' 해시를 구성하는 버킷 '''
    def __init__(self, key: Any = None, value: Any = None,
                 stat: Status = Status.EMPTY) -> None:
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성
    
    def set(self, key: Any, value: Any, stat: Status) -> None:
        self.key = key
        self.value = value
        self.stat = stat
    
    def set_status(self, stat: Status) -> None:
        self.stat = stat

class OpenHash:
    ''' 오픈 주소법으로 구현하는 해시 클래스 '''
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity
    
    def hash_value(self, key: Any) -> int:
        ''' 해시값을 구함 '''
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def rehash_value(self, key: Any) -> int:
        ''' 재해시 값을 구함 '''
        return (self.hash_value(key) + 1) % self.capacity
    
    def search_node(self, key: Any) -> Any:
        ''' 키가 key인 버킷을 검색 '''
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)
            p = self.table[hash]
        
        return None
    
    def search(self, key: Any) -> Any:
        ''' 키가 key인 원소를 검색하여 값을 반환 '''
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None
    
    def add(self, key: Any, value: Any) -> bool:
        ''' 키가 key 이고 값이 value인 원소를 추가 '''
        if self.search(key) is not None:
            return False
        
        hash = self.hash_value(key)
        p = self.table[hash]
        
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        
        return False
    
    def remove(self, key: Any) -> int:
        ''' 키가 key인 원소를 삭제 '''
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True
    
    def dump(self) -> None:
        ''' 해시테이블을 덤프 '''
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 미등록 --')
            elif self.table[i].stat == Status.DELETED:
                print('-- 삭제 완료 --')
    

