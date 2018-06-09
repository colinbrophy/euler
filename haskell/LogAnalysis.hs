{-# OPTIONS_GHC -Wall #-}
module LogAnalysis where

import Log
import Text.Read

tryParse :: String -> Maybe LogMessage
tryParse line = let tokens = words line in
    case tokens of
    "I":_ -> makeMessage Info tokens
    "W":_ -> makeMessage Warning tokens
    "E":level:xs -> do
        nLevel <- readMaybe level
        makeMessage (Error nLevel) xs
    _  -> Nothing

parseMessage :: String -> LogMessage
parseMessage line =
    case tryParse line of
    Just a -> a
    Nothing -> Unknown line

intersperse :: a -> [[a]] -> [a]
intersperse _ [] = [] 
intersperse _ [x] = x
intersperse sep (x:xs) = x ++ [sep] ++ intersperse sep xs

makeMessage :: MessageType -> [String] -> Maybe LogMessage
makeMessage messageType (_:timestamp:lineTail) = do
    time <- readMaybe timestamp
    return $ LogMessage messageType time message
    where message = intersperse ' ' lineTail
makeMessage _ _ = Nothing

{- 
parseMessage line = ==

splitByWord "" = []
splitByWord x = w : spliter x

spliter (x:xs) = case x of
    ' '   -> ("", xs)
    other -> (x : spliter xs, xs)

parseMessageType 'I' = Just Info
parseMessageType 'W' = Just Warning
parseMessageType 'I' = Just Error 
-}