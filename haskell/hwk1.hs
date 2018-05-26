import Data.Char (digitToInt)

toDigits :: (Integral a, Show a) => a -> [a]
toDigits x 
  | x > 0 = map (fromIntegral . digitToInt) . show $ x 
  | otherwise = []

toDigitsRev :: (Integral a, Show a) => a -> [a]
toDigitsRev = reverse . toDigits

doubleEveryOther :: Num a => [a] -> [a]
doubleEveryOther = reverse . doubleFromLeft . reverse
  where doubleFromLeft = zipWith (*) (cycle [1,2])

sumDigits :: (Integral a, Show a) => [a] -> a
sumDigits = sum . concatMap toDigits

validate :: (Integral a, Show a) => a -> Bool
validate = divides 10 . sumDigits . doubleEveryOther . toDigits
  where divides d n = n `mod` d == 0

