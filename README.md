# Duplicates Remover

## Running the script
I provided a CLI-like interface for running the script. The program supports 2 features (but can easily be extended):
1. Duplicates Removing - replaces all duplicates with a .symlink and leaves only one of the copies as the original file
`python3 main.py remove_duplicates --path=<path>`
2. Duplicates Scanner - scans the file system and prints the duplicates to stdout (this is the default implementation)
`python3 main.py identify_duplicates  --path=<path>`

## Notes
### Algorithm Description
The algorithm compares duplicate files based on their content (not much flexibility, it's pretty much an all-or-nothing comparison).
The current implementation reads each file under the provided path and creates a SHA1 hash key to represent its content. SHA1 is known as one of the fastest encryption algorithms (that is also more secure compared to other fast encryption methods such as MD5). Another valuable property that we use here is its "uniqueness" in hashing different strings (not unique, but as a convention, we consider it as it was unique).
I use Hashmap (dictionary) to store each file's data, to make it easier to spot if I encounter a duplicate along with the scanning.

### UML Structure
![UML Structure](https://i.imgur.com/7sUmn12.jpg)

### Design Notes
This system is way over-complicated (or over-engineered) for serving its original purpose, which is identifying and removing duplicates in the system. However, as this is supposed to reflect system engineering skills, I chose to develop it to an extent of some additional flexibility.
The current implementation separates the files scanning logic from the low-level implementation of I/O operations and file tracking (to identify a duplicate).
This allows you to easily adjust the script to apply the logic on files in your cloud or even record the duplicates in an external database.

Also, where the class interface and the class implementation was identical , I chose not to create separate files for the current implementation

### Suggested Improvements
There are more than a few ways to optimize/improve the current implementation, I'll suggest a few:
1. Add-Type hinting for all function/methods. and strictly define interfaces/abstract classes/methods
2. Implement adapters for all cloud services (and use a factory to make it possible to generate a handler for each feature with only one command)
3. Export the script's log to a CSV at the end of the operation
4. Add one more level of abstraction to use the same script to make more than just identify duplicates
5. Refine CLI options to not include unsupported features
6. Filter files - Add an option target/exclude specific files by pattern (for example) and operate only on those who fulfill the predicate (this will optimize RAM in runtime as we don't need to store and operate all files - but in terms of running time, we still need to scan all files)
7. etc.

