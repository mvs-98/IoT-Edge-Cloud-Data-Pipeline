import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    # Prepare data
    data = {
    'Timestamp': ['01/09','02/09','03/09','04/09','05/09'],
    'Value': [1,2,1,10,5]
    }

    data_df = pd.DataFrame(data)
    # Initialize a canvas
    plt.figure(figsize=(8, 4), dpi=200)
    # Plot data into canvas

    plt.plot(data_df["Timestamp"], data_df["Value"], color="#FF3B1D", marker='.', linestyle="-")
    plt.title("Example data for demonstration")
    plt.xlabel("DateTime")
    plt.ylabel("Value")

    # Save as file
    plt.savefig("figure1.png")
    # Directly display
    plt.show()