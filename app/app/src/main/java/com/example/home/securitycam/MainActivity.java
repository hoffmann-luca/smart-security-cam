package com.example.home.securitycam;

import android.app.Activity;
import android.content.Intent;
import android.os.StrictMode;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EdgeEffect;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;

import java.net.Socket;

public class MainActivity extends AppCompatActivity {

    public Button Settings;
    public Button Stream;
    public Button Connect;
    public Button scanqr;

    public EditText IpInput;

    public static TextView IpSaver;

    public static Socket client;
    public String ip;
    public int port = 64932;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Settings = (Button)findViewById(R.id.buttonSettings);
        Stream = (Button)findViewById(R.id.buttonStream);
        Connect = (Button)findViewById(R.id.buttonConnect);
        scanqr = (Button)findViewById(R.id.buttonScan);

        IpInput = (EditText)findViewById(R.id.editTextIp);

        IpSaver = (TextView)findViewById(R.id.textViewIpSaver);

        final Activity activity = this;


        Connect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                IpSaver.setText(IpInput.getText().toString());
                new Connect().execute(IpInput.getText().toString());
                IpInput.setEnabled(false);

            }
        });

        scanqr.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                IntentIntegrator integrator = new IntentIntegrator(activity);
                integrator.setDesiredBarcodeFormats(IntentIntegrator.QR_CODE_TYPES);
                integrator.setPrompt("Scan");
                integrator.setCameraId(0);
                integrator.setBeepEnabled(false);
                integrator.setBarcodeImageEnabled(false);
                integrator.initiateScan();
            }
        });

        Settings.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int ce = v.getId();
                if(ce == R.id.buttonSettings){
                    Intent intent = new Intent(MainActivity.this, MainSettings.class);
                    startActivity(intent);
                }
            }
        });

        Stream.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int ce2 = v.getId();
                if(ce2 == R.id.buttonStream){
                    Intent intent = new Intent(MainActivity.this, MainStream.class);
                    startActivity(intent);
                }
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        IntentResult result = IntentIntegrator.parseActivityResult(requestCode,resultCode,data);
        if(result != null){
            if(result.getContents() == null){
                Toast.makeText(getApplicationContext(), "You cancelled the scanning", Toast.LENGTH_SHORT).show();
            }else {
                if(IpInput.isEnabled())
                    IpInput.setText(result.getContents());
                else{
                    Toast.makeText(getApplicationContext(), "You are already connected to " + IpSaver.getText().toString(), Toast.LENGTH_SHORT).show();
                }
            }
        }else {
            super.onActivityResult(requestCode, resultCode, data);
        }
    }
}
