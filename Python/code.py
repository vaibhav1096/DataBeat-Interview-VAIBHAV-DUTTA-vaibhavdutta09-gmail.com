from enum import Enum
class ADJACENCY(Enum):
	HORIZONTAL=1
	VERTICAL=2
	DIAGONAL=3
	HORIZONTAL_VERTICAL=4
	HORIZONTAL_VERTICAL_DIAGONAL=5

adjacency= int(input())
rows= int(input("Enter number of rows : "))
columns= int(input("Enter number of columns : "))
input_list=[]
ans=0
for i in range(0,rows):
	temp_list=[]
	for j in range(0,columns):
		inp=int(input())
		temp_list.append(inp)

	input_list.append(temp_list)




def dfs_inner(original_matrix,traversal_status,adjacency,row_ind,col_ind,ans):

	if(adjacency==ADJACENCY.HORIZONTAL.value ):
		traversal_status[row_ind][col_ind]=True
		original_matrix[row_ind][col_ind]=ans
		if(col_ind<len(original_matrix[0])-1 and traversal_status[row_ind][col_ind+1]==False and  original_matrix[row_ind][col_ind+1]==1):
			dfs_inner(original_matrix,traversal_status,adjacency,row_ind,col_ind+1,ans)

		if (col_ind -1 >=0 and traversal_status[row_ind][col_ind-1 ] == False and
				original_matrix[row_ind][col_ind -1] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind, col_ind -1, ans)

	if (adjacency == ADJACENCY.VERTICAL.value ):
		traversal_status[row_ind][col_ind] = True
		original_matrix[row_ind][col_ind] = ans
		if (row_ind < len(original_matrix)-1 and traversal_status[row_ind+1][col_ind ] == False and
				original_matrix[row_ind+1][col_ind ] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind+1, col_ind , ans)

		if (row_ind -1 >=0 and traversal_status[row_ind-1][col_ind ] == False and
				original_matrix[row_ind-1][col_ind ] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind-1, col_ind , ans)



	if (adjacency == ADJACENCY.DIAGONAL.value ):
		traversal_status[row_ind][col_ind] = True
		original_matrix[row_ind][col_ind] = ans
		if (row_ind+1 < len(original_matrix) and col_ind+1<len(original_matrix[0]) and traversal_status[row_ind+1][col_ind+1 ] == False and
				original_matrix[row_ind+1][col_ind +1] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind+1, col_ind+1 , ans)

		if (row_ind+1 < len(original_matrix) and col_ind-1>=0 and traversal_status[row_ind+1][col_ind-1 ] == False and
				original_matrix[row_ind+1][col_ind -1] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind+1, col_ind-1 , ans)

		if (row_ind-1 >=0 and col_ind+1<len(original_matrix[0]) and traversal_status[row_ind-1][col_ind+1 ] == False and
				original_matrix[row_ind-1][col_ind +1] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind-1, col_ind+1 , ans)

		if (row_ind-1 >=0 and col_ind-1>=0 and traversal_status[row_ind-1][col_ind-1 ] == False and
				original_matrix[row_ind-1][col_ind-1 ] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind-1, col_ind-1 , ans)


	if(adjacency==ADJACENCY.HORIZONTAL_VERTICAL.value):
		traversal_status[row_ind][col_ind]=True
		original_matrix[row_ind][col_ind]=ans
		if(col_ind<len(original_matrix[0])-1 and traversal_status[row_ind][col_ind+1]==False and  original_matrix[row_ind][col_ind+1]==1):
			dfs_inner(original_matrix,traversal_status,adjacency,row_ind,col_ind+1,ans)

		if (row_ind < len(original_matrix)-1 and traversal_status[row_ind+1][col_ind ] == False and
				original_matrix[row_ind+1][col_ind ] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind+1, col_ind , ans)

		if (row_ind -1 >=0 and traversal_status[row_ind-1][col_ind ] == False and
				original_matrix[row_ind-1][col_ind ] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind-1, col_ind , ans)

		if (col_ind -1 >=0 and traversal_status[row_ind][col_ind-1 ] == False and
				original_matrix[row_ind][col_ind -1] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind, col_ind -1, ans)


	if(adjacency==ADJACENCY.HORIZONTAL_VERTICAL_DIAGONAL.value):
		traversal_status[row_ind][col_ind] = True
		original_matrix[row_ind][col_ind] = ans
		if (row_ind+1 < len(original_matrix) and col_ind+1<len(original_matrix[0]) and traversal_status[row_ind+1][col_ind+1 ] == False and
				original_matrix[row_ind+1][col_ind +1] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind+1, col_ind+1 , ans)

		if (row_ind+1 < len(original_matrix) and col_ind-1>=0 and traversal_status[row_ind+1][col_ind-1 ] == False and
				original_matrix[row_ind+1][col_ind -1] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind+1, col_ind-1 , ans)

		if (row_ind-1 >=0 and col_ind+1<len(original_matrix[0]) and traversal_status[row_ind-1][col_ind+1 ] == False and
				original_matrix[row_ind-1][col_ind +1] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind-1, col_ind+1 , ans)

		if (row_ind-1 >=0 and col_ind-1>=0 and traversal_status[row_ind-1][col_ind-1 ] == False and
				original_matrix[row_ind-1][col_ind-1 ] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind-1, col_ind-1 , ans)

		if (col_ind < len(original_matrix[0]) - 1 and traversal_status[row_ind][col_ind + 1] == False and
				original_matrix[row_ind][col_ind + 1] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind, col_ind + 1, ans)

		if (row_ind < len(original_matrix) - 1 and traversal_status[row_ind + 1][col_ind] == False and
				original_matrix[row_ind + 1][col_ind] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind + 1, col_ind, ans)

		if (row_ind -1 >=0 and traversal_status[row_ind-1][col_ind ] == False and
				original_matrix[row_ind-1][col_ind ] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind-1, col_ind , ans)

		if (col_ind -1 >=0 and traversal_status[row_ind][col_ind-1 ] == False and
				original_matrix[row_ind][col_ind -1] == 1):
			dfs_inner(original_matrix, traversal_status, adjacency, row_ind, col_ind -1, ans)






def dfs_caller(original_matrix,traversal_status,adjacency):
	for i in range(0,len(original_matrix)):
		#what if no rows are present
		for j in range(0,len(original_matrix[0])):
			if(traversal_status[i][j]==False and original_matrix[i][j]==1):
				global ans
				ans=ans+1
				dfs_inner(original_matrix,traversal_status,adjacency,i,j,ans)



def mainfunction():
	if(rows==0 or columns==0):
		return
	traversal_status=[[False for j in range(columns)] for i in range(rows)]
	dfs_caller(input_list,traversal_status,5)



mainfunction()
print(ans)