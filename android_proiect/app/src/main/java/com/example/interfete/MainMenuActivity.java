package com.example.interfete;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;

public class MainMenuActivity extends BaseActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_menu);
        setupToolbar(getString(R.string.main_menu_title));

        Button goDataButton = findViewById(R.id.goDataButton);
        Button goQuizButton = findViewById(R.id.goQuizButton);
        Button goInfoButton = findViewById(R.id.goInfoButton);
        Button goHelpButton = findViewById(R.id.goHelpButton);
        Button logoutButton = findViewById(R.id.logoutButton);

        goDataButton.setOnClickListener(view -> startActivity(new Intent(this, DataManagementActivity.class)));
        goQuizButton.setOnClickListener(view -> startActivity(new Intent(this, QuizActivity.class)));
        goInfoButton.setOnClickListener(view -> startActivity(new Intent(this, InfoActivity.class)));
        goHelpButton.setOnClickListener(view -> startActivity(new Intent(this, HelpActivity.class)));
        logoutButton.setOnClickListener(view -> finish());
    }
}
