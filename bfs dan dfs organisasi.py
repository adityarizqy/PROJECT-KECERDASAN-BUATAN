organisasi =  {'rektor':set(['pembina']),
         'pembina':set(['rektor','ketua']),
         'ketua':set(['pembina','wakil','sekretaris','bendahara', 'humas']),
         'sekretaris':set(['ketua','humas','bendahara', 'litbang']),
         'bendahara':set(['ketua', 'sekretaris', 'kas', 'event']),
         'kas':set(['bendahara', 'event']),
         'event':set(['bendahara', 'kas']),
         'wakil':set(['ketua']),
         'humas':set(['ketua', 'sekretaris', 'peralatan', 'perlengkapan', 'humas intern', 'humas ekstern']),
         'humas intern':set(['humas','humas ekstern']),
         'humas ekstern':set(['humas','humas intern']),
         'perlengkapan':set(['humas', 'peralatan']),
         'peralatan':set(['humas', 'perlengkapan']),
         'litbang':set(['sekretaris', 'penelitian', 'pengembangan']),
         'penelitian':set(['litbang','pengembangan']),
         'pengembangan':set(['litbang','penelitian']),
        
         
         }
def bfs(graf,mulai,tujuan):
    
    queue = [[mulai]]
    visited = set()

    while queue:     
       
        jalur = queue.pop(0)

        
        state = jalur[-1]
        if state == tujuan:        
            return jalur       
        elif state not in visited:
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                queue.append(jalur_baru) 

           
            visited.add(state)

        
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")

def dfs(graf, mulai, tujuan):
    stack = [[mulai]]
    visited = set()

    while stack:
        
        panjang_tumpukan = len(stack)-1
        
       
        jalur = stack.pop(panjang_tumpukan)

        
        state = jalur[-1]

        
        if state == tujuan:
            return jalur
        
        elif state not in visited:
            
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                stack.append(jalur_baru)

            
            visited.add(state)


        
        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")
