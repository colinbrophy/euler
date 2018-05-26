import Data.Char (digitToInt)

toDigits :: (Integral a, Show a) => a -> [a]
toDigits x 
  | x > 0 = map (fromIntegral . digitToInt) . show $ x 
  | otherwise = []
-- toDigits x  
--  | x <= 0 = []
--  | otherwise = toDigits (x `div` 10) ++ [x `mod` 10] 

toDigitsRev :: (Integral a, Show a) => a -> [a]
toDigitsRev = reverse . toDigits

doubleEveryOther :: Num a => [a] -> [a]
-- doubleEveryOther [] = []
-- doubleEveryOther x = doubleEveryOther (init (init x)) ++ [last (init x)] ++ [(last x)  * 2]
-- Much easier to work with lists from the left in haskell (infinte lists etc)
doubleEveryOther = reverse . doubleFromLeft . reverse
  where doubleFromLeft = zipWith (*) (cycle [1,2])
