Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: D:\Pooja\MSC\Pracs\Bioinformatics\BioInformatics_Prac1_PairwiseAlignment.py 
Enter the first sequence::abcvfdg
Enter the second sequence::abvgcfd

['a', 'b', 'c', 'v', 'f', 'd', 'g']
['a', 'b', 'v', 'g', 'c', 'f', 'd']
['1', '1', '0', '0', '0', '0', '0']
2
>>> 
>>> 
>>> 
>>> 
 RESTART: D:\Pooja\MSC\Pracs\Bioinformatics\BioInformatics_Prac1_PairwiseAlignment.py 
Enter the first sequence::abcvfdg
Enter the second sequence::abvgcf
Enter the position to insert::2
['a', 'b', 'c', 'v', 'f', 'd', 'g']
['a', 'b', '-', 'v', 'g', 'c', 'f']
['1', '1', '0', '1', '0', '0', '0']
3
>>> 
>>> 
>>> 
>>> 
 RESTART: D:\Pooja\MSC\Pracs\Bioinformatics\Bioinformatics_Prac2_IdentityValue.py 
Enter the first sequence::abcvfdg
Enter the second sequence::abvgcfd

abcvfdg
['a', 'b', 'v', 'g', 'c', 'f', 'd']
Matching Score:: 7
Identity of the sequences:: 14.285714285714285
>>> 
>>> 
>>> 
>>> 
 RESTART: D:\Pooja\MSC\Pracs\Bioinformatics\Bioinformatics_Prac2_IdentityValue.py 
Enter the first sequence::abcvfdg
Enter the second sequence::abcfgv
Enter the position to insert gap::3
abcvfdg
['a', 'b', 'c', '-', 'f', 'g', 'v']
Matching Score:: 6
Identity of the sequences:: 12.244897959183673
>>> 
>>> 
>>> 
>>> 
 RESTART: D:\Pooja\MSC\Pracs\Bioinformatics\Bioinformatics_Prac3_SimilarityValue.py 
Enter the first sequence::abcvdgfhijk
Enter the second sequence::abgcvfghji
How many elements for similarity condition?2
Enter an element: a
How many elements is it similar to?2
What is it similar to?j
What is it similar to?i
Enter an element: c
How many elements is it similar to?3
What is it similar to?v
What is it similar to?f
What is it similar to?g
['a', 'b', 'c', 'v', 'd', 'g', 'f', 'h', 'i', 'j', 'k']
['a', 'b', 'g', 'c', 'v', 'f', 'g', 'h', 'j', 'i']
[['a', 'j', 'i'], ['c', 'v', 'f', 'g']]
54.54545454545455 %
>>> 
