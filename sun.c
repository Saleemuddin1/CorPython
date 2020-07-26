  #include <stdio.h>
  #include <string.h>
  #define MAXIMUM 256

  int main() {
        int val;
        FILE *file1, *file2;
        char ch,s, src[MAXIMUM], tgt[MAXIMUM];
        file1 = fopen ("/home/saleemuddin1/CorPy/leapYear.py","r");
        /* handle error */
        if (!file1) {
                printf("Unable to open input file!\n");
                return 0;
        }
        file2 = fopen("/home/saleemuddin1/CorPy/result3.bin", "wb");

        /*handle error */
        if (!file2) {
                printf("Unable to open output file!\n");
                return 0;
        }
        while (s =fgetc(file1) != EOF) {
                /* reading 1 data byte */
                fread(&ch, sizeof(char), 1, file1);
                val = ch; 
                fwrite(&val, sizeof(int), 1, file2);
        }

        /* close the files */
        fclose(file1);
        fclose(file2);
        printf("Please Check Binary File Contents in File: result3.bin\n");
	return 0;
  }


