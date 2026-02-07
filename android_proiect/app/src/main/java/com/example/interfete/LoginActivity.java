package com.example.interfete;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

public class LoginActivity extends BaseActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        setupToolbar(getString(R.string.login_title));

        Button loginButton = findViewById(R.id.loginButton);
        TextView loginHint = findViewById(R.id.loginHint);
        loginHint.setText("Autentifică-te pentru a accesa toate modulele aplicației.");

        loginButton.setOnClickListener(view -> {
            Intent intent = new Intent(LoginActivity.this, MainMenuActivity.class);
            startActivity(intent);
        });
    }
}
