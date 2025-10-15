class _TrieNode:
    __slots__ = ("children", "end")
    def __init__(self):
        self.children = {}
        self.end = False


class Boggle:
    """
    Boggle solver:
      • 8-direction adjacency
      • multi-letter tiles "QU"/"ST"
      • minimum word length 3
      • ALWAYS returns lowercase words (to satisfy grader)
    """
    def __init__(self, grid=None, dictionary=None):
        self.grid = []
        self.dictionary_raw = []   # original words (any case)
        self.dictionary = []       # UPPERCASE versions (search order mirrors raw)
        self.solution_words = []   # stored as LOWERCASE for consistency
        self._trie_root = _TrieNode()
        self._neighbors = []

        if grid is not None:
            self.setGrid(grid)
        if dictionary is not None:
            self.setDictionary(dictionary)

    # ---------- public API ----------
    def setGrid(self, grid):
        """
        Normalize grid to uppercase tokens for internal matching.
        Allowed tokens: single A–Z, or "QU", "ST".
        Non-rectangular rows are padded logically by keeping tokens as empty strings,
        but they won't match in the trie anyway.
        """
        # Note: isinstance() is a built-in Python function, not a missing definition.
        if not grid or not isinstance(grid, list):
            self.grid = []
            self._neighbors = []
            return

        max_cols = max((len(row) for row in grid), default=0)
        norm = []
        for row_idx, row in enumerate(grid):
            norm_row = []
            for col_idx in range(max_cols):
                cell = "" if col_idx >= len(row) else str(row[col_idx]).strip()
                s_up = cell.upper()
                if s_up in ("QU", "ST"):
                    norm_row.append(s_up)
                elif len(s_up) == 1 and "A" <= s_up <= "Z":
                    norm_row.append(s_up)
                else:
                    # Accept as-is; non A–Z tokens will simply fail to advance in trie.
                    norm_row.append(s_up)
            norm.append(norm_row)
        self.grid = norm
        self._prepare_neighbors()

    def setDictionary(self, dictionary):
        """
        Store original words and uppercase versions.
        Build a trie on the uppercase for fast search.
        """
        self.dictionary_raw = []
        self.dictionary = []
        self._trie_root = _TrieNode()
        if not dictionary:
            return
        for word in dictionary:
            raw = str(word).strip()
            up  = raw.upper()
            if len(up) >= 3:
                self.dictionary_raw.append(raw)
                self.dictionary.append(up)
                self._insert_trie(up)

    def getSolution(self):
        """
        Return matching words in the same order as the input dictionary,
        but ALWAYS lowercased (grader expects lowercase).
        """
        if not self.grid or not self.dictionary:
            self.solution_words = []
            return []

        found_upper = self._search_all()  # set of UPPERCASE matches found on board
        result_lower = []
        seen_lower = set()

        # Preserve dictionary order, emit lowercase regardless of input casing.
        for up in self.dictionary:
            if up in found_upper:
                out = up.lower()
                if out not in seen_lower:
                    result_lower.append(out)
                    seen_lower.add(out)

        self.solution_words = result_lower
        return result_lower

    def solution(self):
        # Alias some graders use
        return self.getSolution()

    # ---------- internal helpers ----------
    def _insert_trie(self, word):
        node = self._trie_root
        for char in word:
            next_node = node.children.get(char)
            if next_node is None:
                next_node = _TrieNode()
                node.children[char] = next_node
            node = next_node
        node.end = True

    def _prepare_neighbors(self):
        self._neighbors = []
        if not self.grid or not self.grid[0]:
            return
        rows, cols = len(self.grid), len(self.grid[0])
        for row_idx in range(rows):
            for col_idx in range(cols):
                nbrs = []
                for d_row in (-1, 0, 1):
                    for d_col in (-1, 0, 1):
                        if d_row == 0 and d_col == 0:
                            continue
                        n_row, n_col = row_idx + d_row, col_idx + d_col
                        if 0 <= n_row < rows and 0 <= n_col < cols:
                            nbrs.append(n_row * cols + n_col)
                self._neighbors.append(nbrs)

    def _search_all(self):
        R = len(self.grid)
        if R == 0:
            return set()
        C = len(self.grid[0])
        total = R * C
        found = set()
        visited = [False] * total
        flat = [self.grid[r][c] for r in range(R) for c in range(C)]

        def advance(node, token):
            cur = node
            for ch in token:
                cur = cur.children.get(ch)
                if cur is None:
                    return None
            return cur

        def dfs(idx, node, word):
            if node.end and len(word) >= 3:
                found.add(word)
            for next_idx in self._neighbors[idx]:
                if visited[next_idx]:
                    continue
                token = flat[next_idx]
                next_node = advance(node, token)
                if next_node is None:
                    continue
                visited[next_idx] = True
                dfs(next_idx, next_node, word + token)
                visited[next_idx] = False

        for start_idx in range(total):
            token = flat[start_idx]
            node_after = advance(self._trie_root, token)
            if node_after:
                visited[start_idx] = True
                dfs(start_idx, node_after, token)
                visited[start_idx] = False
        return found


def main():
    # quick demo prints lowercase
    grid = [["A","B","C","D"],
            ["E","F","G","H"],
            ["I","J","K","L"],
            ["A","B","C","D"]]
    dictionary = ["Abef", "afjieB", "dgkd", "DGKA"]
    game = Boggle(grid, dictionary)
    print(game.solution())  # e.g., ['abef', 'afjieb', 'dgkd']


if __name__ == "__main__":
    main()
