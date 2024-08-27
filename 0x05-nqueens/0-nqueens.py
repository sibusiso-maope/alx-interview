#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    backtrack function to find solution
    """
    if r == n:
        res = []
        for k in range(len(board)):
            for l in range(len(board[k])):
                if board[k][l] == 1:
                    res.append([k, l])
        print(res)
        return

    for m in range(n):
        if m in cols or (r + m) in pos or (r - m) in neg:
            continue

        cols.add(m)
        pos.add(r + m)
        neg.add(r - m)
        board[r][m] = 1

        backtrack(r+1, n, cols, pos, neg, board)

        cols.remove(m)
        pos.remove(r + m)
        neg.remove(r - m)
        board[r][m] = 0


def nqueens(n):
    """
    Solution to nqueens problem
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
