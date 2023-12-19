class Bitset:
    
      def __init__(self, size: int):
        self.original = ['0'] * size  
        self.reversed = ['1'] * size 
        self.cnt = 0

      def fix(self, idx: int) -> None:
        if self.original[idx] == '0':
          self.cnt += 1
        self.original[idx] = '1'
        self.reversed[idx] = '0'

      def unfix(self, idx: int) -> None:
        if self.original[idx] == '1':
          self.cnt -= 1
        self.original[idx] = '0'
        self.reversed[idx] = '1'

      def flip(self) -> None:
        self.original, self.reversed = self.reversed, self.original
        self.cnt = len(self.original) - self.cnt

      def all(self) -> bool:
        return self.cnt == len(self.original)

      def one(self) -> bool:
        return self.cnt

      def count(self) -> int:
        return self.cnt

      def toString(self) -> str:
        return ''.join(self.original)