package com.example.interfete;

import android.os.Bundle;
import android.widget.Button;
import android.widget.RadioGroup;
import android.widget.Toast;

public class QuizActivity extends BaseActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_quiz);
        setupToolbar(getString(R.string.quiz_title));

        RadioGroup quizGroup = findViewById(R.id.quizGroup);
        Button submitQuizButton = findViewById(R.id.submitQuizButton);
        Button backToMenuButton = findViewById(R.id.backToMenuButton);

        submitQuizButton.setOnClickListener(view -> {
            int selectedId = quizGroup.getCheckedRadioButtonId();
            if (selectedId == -1) {
                Toast.makeText(this, "Selectează un răspuns.", Toast.LENGTH_SHORT).show();
                return;
            }
            Toast.makeText(this, "Răspunsul a fost înregistrat.", Toast.LENGTH_SHORT).show();
        });

        backToMenuButton.setOnClickListener(view -> finish());
    }
}
