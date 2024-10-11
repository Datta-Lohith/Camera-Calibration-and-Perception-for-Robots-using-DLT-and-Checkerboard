import numpy as np

# Image points
image_points = np.array([[757, 213], [758, 415], [758, 686], [759, 966],
                         [1190, 172], [329, 1041], [1204, 850], [340, 159]])

# World points
world_points = np.array([[0, 0, 0], [0, 3, 0], [0, 7, 0], [0, 11, 0],
                         [7, 1, 0], [0, 11, 7], [7, 9, 0], [0, 1, 7]])

def decompose_P(P):
    # Implementing Gram-Schmidt process to decompose P matrix for Intrinsic and Extrinsic parameters
    P_k = P[:, :3].copy()
    
    # Number of rows and columns
    n, m = P_k.shape
    
    # Empty Matrices for Rotation(R) and Intrinsic parameters(K) matrices
    R = np.zeros((n, m))
    K = np.zeros((m, m))
    
    # Gram-Schmidt process
    v= P_k[:, 0]
    K[0, 0] = np.linalg.norm(v)
    R[:, 0] = v/K[0, 0]
    
    for j in range(1, m):
        v = P_k[:, j]
        for i in range(j):
            K[i, j] = np.dot(R[:, i], P_k[:, j])
            proj = K[i,j]/np.dot(R[:, i], R[:, i])
            v -= proj * R[:, i]
        K[j, j] = np.linalg.norm(v)
        R[:, j] = v / K[j, j]
    
    # Normalizing K matrix in last column
    K = K/K[2,2]
    
    # Decomposing P matrix for Translation vector(T)
    T= (np.linalg.inv(K) @ P[:,3])
    T.shape = (3,1)
    return R,K,T

def find_P_matrix(image_points, world_points):
        
    # Convert to homogeneous coordinates
    image_points_hom = np.hstack((image_points, np.ones((8, 1))))
    world_points_hom = np.hstack((world_points, np.ones((8, 1))))

    # Define A matrix
    A=[]
    for i in range(len(image_points_hom)):
        A.append(np.hstack((world_points_hom[i], np.zeros(4), -image_points_hom[i, 0] * world_points_hom[i])))
        A.append(np.hstack((np.zeros(4), world_points_hom[i], -image_points_hom[i, 1] * world_points_hom[i])))

    # Use SVD to solve for P
    _, _, V = np.linalg.svd(A)
    P = V[-1, :].reshape((3, 4))

    # Verify that the projection is accurate
    image_points_pred = np.dot(world_points_hom, P.T)
    image_points_pred /= image_points_pred[:, 2][:, np.newaxis]
    errors = image_points_pred - image_points_hom

    return P,errors


if __name__ == "__main__":
    # Find P matrix
    P,E = find_P_matrix(image_points, world_points)
    print("P matrix:\n", P)
    
    # Decompose P matrix for Intrinsic and Extrinsic parameters    
    R,K,T = decompose_P(P)
    print("\nK matrix:\n", K)
    print("\nRotation matrix:\n", R)
    print("\nTranslation vector:\n", T)

    print("\nReprojection error for each point:\n\n   Point\t\t\tError")
    # Reprojection error for each point
    for i in range(len(E)):
        print(f"{image_points[i]} \t:\t {np.linalg.norm(E[i])}\n")
    