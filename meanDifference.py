def md_nre_single_sample(y, y_hat, n, p):
    # Calculate the nth root of y and y_hat
    nth_root_y = y**(1/n)
    nth_root_y_hat = y_hat**(1/n)
    
    # Calculate the difference and raise it to the power of p
    loss = abs(nth_root_y - nth_root_y_hat)**p
    
    return loss

# Test examples
print(f"md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1) >> {md_nre_single_sample(100, 99.5, 2, 1)}")
print(f"md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1) >> {md_nre_single_sample(50, 49.5, 2, 1)}")
print(f"md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1) >> {md_nre_single_sample(20, 19.5, 2, 1)}")
print(f"md_nre_single_sample(y=5.5, y_hat=5, n=2, p=1) >> {md_nre_single_sample(5.5, 5, 2, 1)}")
print(f"md_nre_single_sample(y=1, y_hat=0.5, n=2, p=1) >> {md_nre_single_sample(1, 0.5, 2, 1)}")
print(f"md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1) >> {md_nre_single_sample(0.6, 0.1, 2, 1)}")
