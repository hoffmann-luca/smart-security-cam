package com.example.home.securitycam;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;


public class MainSettings extends AppCompatActivity {

    public Button back;
    public Button send;

    public EditText email;
    public EditText wlankey;

    private String ip;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);

        back = (Button)findViewById(R.id.buttonBackHome);
        send = (Button)findViewById(R.id.buttonSendSettings);

        email = (EditText)findViewById(R.id.editTextEmail);
        wlankey = (EditText)findViewById(R.id.editTextWlanKey);

        send.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!email.getText().toString().isEmpty() /*&& !wlankey.getText().toString().isEmpty()*/) {
                    ip = MainActivity.IpSaver.getText().toString();
                    new Connect().execute(ip,email.getText().toString()/*,wlankey.getText().toString()*/);
                    email.getText().clear();
                    wlankey.getText().clear();
                    Toast.makeText(getApplicationContext(),"Settings saved...", Toast.LENGTH_SHORT).show();
                }else{
                    Toast.makeText(getApplicationContext(), "The Settings are not complete!", Toast.LENGTH_SHORT).show();
                }
            }
        });

        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });
    }
}
