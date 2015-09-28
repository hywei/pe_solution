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


-- solution 001 --
res_001 = foldl step 0 [0..999]
    where step x y = if (y `mod` 3 == 0 || y `mod` 5 == 0) then x + y else x

-- solution 002 --     
res_002 = sum (filter even (takeWhile (<4000000) fibs))

-- solution 003 --
res_003 = last $ primer_factors 600851475143 

-- solution 004 -- 
ps []       = []
ps (x:xs)  = primer_factors x ++ (ps xs)

-- solution 004 --
is_palindrome :: (Integral a) => a -> Bool 



-- solution 006 --
res_006 = (sum [1..100] ^ 2) - (sum (map (\x-> x * x) [1..100])) 

-- solution 007
res_007 = last $ take 10001 primers

-- solution 010
res_010 = sum $ takeWhile (<2000000) primers

-- solution 016 
res_016 = sumDigits (2 ^ 1000)
    where sumDigits x 
            | x < 10    = x
            | otherwise = (x `mod` 10) + (sumDigits $ x `div` 10)
