package com.example.wordlesolver;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

/*this class simply takes a wordlist input from the user and transfer it to the main activity*/
public class AddWordlist extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_wordlist);

        EditText wordlistEditText = (EditText) findViewById(R.id.wordlistEditText);
        Button enterWordlistButton = (Button) findViewById(R.id.enterWordlistButton);
        enterWordlistButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String newWordlist = wordlistEditText.getText().toString();
                if(!newWordlist.equals("")) {
                    String[] newWordlistArray = newWordlist.split(",");

                    Intent intent = new Intent(AddWordlist.this, MainActivity.class);
                    intent.putExtra("key", newWordlistArray);
                    finish();
                    AddWordlist.this.startActivity(intent);
                }
                finish();
            }
        });

    }


}