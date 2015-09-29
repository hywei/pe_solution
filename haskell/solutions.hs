{-# LANGUAGE FlexibleInstances #-}

import Data.List

fibs :: (Integral a) => [a]
fibs = 1 : 2 : zipWith (+) fibs (tail fibs)

simple_primers :: (Integral a) => [a]
simple_primers = sieve [2..]
    where sieve (p : xs) = p : sieve [ x | x <- xs, x `mod` p /= 0]

-- better primers http://en.literateprograms.org/Sieve_of_Eratosthenes_(Haskell)
primers:: (Integral a) => [a]
nonprimers :: (Integral a) => [a]

primers = [2, 3, 5] ++ (diff [7, 9 ..] nonprimers)
nonprimers = foldr1 f $ map g $ tail primers
    where 
        f (x:xt) ys = x : (merge xt ys)
        g p         = [ n * p | n <- [p, p+2 ..]]

merge :: (Ord a) => [a] -> [a] -> [a]
merge xs@(x:xt) ys@(y:yt) = 
    case compare x y of 
        LT -> x : (merge xt ys)
        EQ -> x : (merge xt yt)
        GT -> y : (merge xs yt)

diff :: (Ord a) => [a] -> [a] -> [a]
diff xs@(x:xt) ys@(y:yt) = 
    case compare x y of
        LT -> x : (diff xt ys)
        EQ -> diff xt yt
        GT -> diff xs yt                

coff :: (Integral a) => a -> a -> a
coff x y 
    | x `mod` y > 0 = 0
    | otherwise     = 1 + (coff (x `div` y)  y)


primer_factors :: (Integral a) => a -> [(a, a)]
primer_factors n = primer_factors_helper n primers
    where primer_factors_helper n (x:xs) 
            | (n == 1)          = []
            | n `mod` x == 0    = let a = coff n x
                                  in (x, a) : primer_factors_helper (n `div` (x^a)) xs
            | otherwise         = primer_factors_helper n xs                            

-- palindrome class
class (Show a) => Palindrome a where
    is_palindrome :: a->Bool
    is_palindrome x = is_palindrome $ show x

instance Palindrome String where
    is_palindrome []        = True
    is_palindrome [x]       = True
    is_palindrome (x:xs)
        | x == last xs      = is_palindrome $ init xs
        | otherwise         = False

instance Palindrome Integer where
    is_palindrome x = is_palindrome $ show x  

instance Palindrome Int where
    is_palindrome x = is_palindrome $ show x    


-- solution 001 --
res_001 = foldl step 0 [0..999]
    where step x y = if (y `mod` 3 == 0 || y `mod` 5 == 0) then x + y else x

-- solution 002 --     
res_002 = sum (filter even (takeWhile (<4000000) fibs))

-- solution 003 --
res_003 = last $ primer_factors 600851475143 

-- solution 004 --
res_004 = head $ sortBy cmp $ filter (is_palindrome . toInteger) [ (x*y) | x <- [999, 998..100], y<-[x, x-1..100]]
            where cmp x y 
                    | x > y     = LT
                    | x < y     = GT
                    | x == y    = EQ

-- solution 005 -- 
ps []       = []
ps (x:xs)  = primer_factors x ++ (ps xs)

-- solution 006 --
res_006 = (sum [1..100] ^ 2) - (sum (map (\x-> x * x) [1..100])) 

-- solution 007
res_007 = last $ take 10001 primers

-- solution 009
triplet = head $ filter helper [(x, y) | x <- [1..1000], y<-[x+1..1000], x+2*y < 1000]
                         where helper v = let 
                                            a = fst v
                                            b = snd v
                                            c = (1000 - a - b)
                                          in a * a + b * b == c * c

res_009 = let a = fst triplet
              b = snd triplet
              c = 1000 - a - b
          in a*b*c                                        
            

-- solution 010
res_010 = sum $ takeWhile (<2000000) primers

-- solution 014
collatz :: (Integral a) => a -> [a]
collatz 1 = [1]
collatz x 
    | even x    = x : (collatz $ x `div` 2)
    | otherwise = x : collatz (3*x + 1)

-- solution 016 
res_016 = sumDigits (2 ^ 1000)
    where sumDigits x 
            | x < 10    = x
            | otherwise = (x `mod` 10) + (sumDigits $ x `div` 10)

