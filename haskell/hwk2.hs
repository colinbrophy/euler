import Data.List (sortBy)

colLen :: Num b => [a] -> b
colLen [] = 0
colLen (_:xs) = 1 + colLen xs 

meanList :: Fractional a => [a] -> a
meanList xs = (sum xs) / (fromIntegral $ length xs)

toPalindrome :: [a] -> [a]
toPalindrome xs = xs ++ reverse xs

palindrome :: Eq a => [a] -> Bool
palindrome xs = xs == reverse xs

sortLen :: [[a]] -> [[a]]
sortLen = sortBy cmpLen where
  cmpLen x y 
    | length x < length y = LT
    | length x > length y = GT
    | otherwise = EQ

intersperse :: a -> [[a]] -> [a]
intersperse _ [] = [] 
intersperse _ [x] = x
intersperse sep (x:xs) = x ++ (sep : intersperse sep xs)

data Tree a = Node a (Tree a) (Tree a)
            | Empty
            deriving (Show)

height :: Tree a -> Integer
height Empty = 0
height (Node _ a b) = succ $ max (height a) (height b)

data Point = Point {
            x :: Integer,
            y :: Integer
}

-- direction a b c = (x b - x a) (y)

-- if (y > mx + c) left
--   otherwi right

-- y a - m x a = y b - m x b
-- y1 = m.x1 + c
-- y2 = mx2 + c
-- y1 + y2 = ((y1 - y2)/ (x1 - x2))(x1 + x2) + 2c

-- y1 + y2 - m(x1 + x2) = 2c


-- m = (y1 - y2)/ (x1 - x2)
-- c = y1 