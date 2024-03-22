from collections import defaultdict, deque

def solution(game_board, table):
    answer = 0
    
    def bfs(graph,v,visited,find=1):
        queue = deque()
        queue.append(v)
        cnt = 0
        x,y = v
        min_x,max_x,min_y,max_y = x,x,y,y
        visited[x][y] = 1
        
        while queue:
            x,y = queue.popleft()
            cnt += 1
            min_x,max_x = min(min_x,x), max(max_x,x)
            min_y,max_y = min(min_y,y), max(max_y,y)
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_x,new_y = x+dx,y+dy
                if new_x<0 or new_y<0 or new_x>=N or new_y>=N:
                    continue
                if not visited[new_x][new_y] and graph[new_x][new_y]==find:
                    visited[new_x][new_y] = 1
                    queue.append((new_x,new_y))
                    
        piece = [tuple(graph[x][y] for y in range(min_y,max_y+1)) for x in range(min_x,max_x+1)]
        return cnt, piece, visited
    
    
    N = len(game_board)
    game_board_dict = defaultdict(list); table_dict = defaultdict(list)
    visited_game_board = [[0 for _ in range(N)] for _ in range(N)]
    visited_table = [[0 for _ in range(N)] for _ in range(N)]
    
    game_board = [[1-game_board[x][y] for y in range(N)] for x in range(N)]
    
    
    for x in range(N):
        for y in range(N):
            if not visited_game_board[x][y] and game_board[x][y]==1:
                cnt,piece,visited_game_board = bfs(game_board,(x,y),visited_game_board,1)
                game_board_dict[cnt].append(piece)
            if not visited_table[x][y] and table[x][y]==1:
                cnt,piece,visited_table = bfs(table,(x,y),visited_table,1)
                table_dict[cnt].append(piece)
    
    
    def match(table_piece,game_piece):
        for _ in range(4):
            if table_piece == game_piece:
                return True
            table_piece = list(zip(*table_piece[::-1]))
        return False
    
    for cnt in game_board_dict.keys():
        game_pieces = game_board_dict[cnt]
        table_pieces = table_dict[cnt]
        visited = [0 for _ in range(len(game_pieces))]
        
        for table_piece in table_pieces:
            flag = 1
            for game_id,game_piece in enumerate(game_pieces):
                if not visited[game_id] and flag:
                    if match(table_piece,game_piece):
                        visited[game_id] = 1
                        answer += cnt
                        flag = 0

    

            
    return answer