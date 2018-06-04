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


