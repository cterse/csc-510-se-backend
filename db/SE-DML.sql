USE dbms;

DELETE FROM USER_RECIPES;
DELETE FROM USERS;
DELETE FROM RECIPES;

INSERT INTO USERS (USER_ID, USER_EMAIL, USER_PASSWORD, SIGNUP_DATE) VALUES (1, 'a@b.com', 'pass123', SYSDATE());
INSERT INTO USERS (USER_ID, USER_EMAIL, USER_PASSWORD, SIGNUP_DATE) VALUES (2, 'c@d.com', 'pass123', SYSDATE());
INSERT INTO USERS (USER_ID, USER_EMAIL, USER_PASSWORD, SIGNUP_DATE) VALUES (3, 'e@f.com', 'pass123', SYSDATE());


INSERT INTO RECIPES (RECIPE_ID, RECIPE_TITLE, RECIPE_INGREDIENTS, RECIPE_PROCEDURE, RECIPE_IMAGE ) VALUES (1, 'RECIPE TITLE 1', 'ING. 1, ING. 2, ING. 3', 'Melt butter in a large, heavy saucepan over medium heat. Add mushrooms, onion, and garlic; cook and stir until tender, about 10 minutes. Add salt, pepper, and thyme; cook and stir until combined, about 1 minute. Stir in chicken broth, heavy cream, and cream cheese. Reduce heat to a low simmer and pour in sherry. Cook, stirring constantly, until flavors are well incorporated, about 45 minutes.', null);
INSERT INTO RECIPES (RECIPE_ID, RECIPE_TITLE, RECIPE_INGREDIENTS, RECIPE_PROCEDURE, RECIPE_IMAGE ) VALUES (2, 'RECIPE TITLE 2', 'ING. 1, ING. 2, ING. 3', 'Melt butter in a large, heavy saucepan over medium heat. Add mushrooms, onion, and garlic; cook and stir until tender, about 10 minutes. Add salt, pepper, and thyme; cook and stir until combined, about 1 minute. Stir in chicken broth, heavy cream, and cream cheese. Reduce heat to a low simmer and pour in sherry. Cook, stirring constantly, until flavors are well incorporated, about 45 minutes.', null);
INSERT INTO RECIPES (RECIPE_ID, RECIPE_TITLE, RECIPE_INGREDIENTS, RECIPE_PROCEDURE, RECIPE_IMAGE ) VALUES (3, 'RECIPE TITLE 3', 'ING. 1, ING. 2, ING. 3', 'Melt butter in a large, heavy saucepan over medium heat. Add mushrooms, onion, and garlic; cook and stir until tender, about 10 minutes. Add salt, pepper, and thyme; cook and stir until combined, about 1 minute. Stir in chicken broth, heavy cream, and cream cheese. Reduce heat to a low simmer and pour in sherry. Cook, stirring constantly, until flavors are well incorporated, about 45 minutes.', null);
INSERT INTO RECIPES (RECIPE_ID, RECIPE_TITLE, RECIPE_INGREDIENTS, RECIPE_PROCEDURE, RECIPE_IMAGE ) VALUES (4, 'RECIPE TITLE 4', 'ING. 1, ING. 2, ING. 3', 'Melt butter in a large, heavy saucepan over medium heat. Add mushrooms, onion, and garlic; cook and stir until tender, about 10 minutes. Add salt, pepper, and thyme; cook and stir until combined, about 1 minute. Stir in chicken broth, heavy cream, and cream cheese. Reduce heat to a low simmer and pour in sherry. Cook, stirring constantly, until flavors are well incorporated, about 45 minutes.', null);


INSERT INTO USER_RECIPES (USER_ID, RECIPE_ID) VALUES (1, 1);
INSERT INTO USER_RECIPES (USER_ID, RECIPE_ID) VALUES (1, 2);
INSERT INTO USER_RECIPES (USER_ID, RECIPE_ID) VALUES (2, 3);
INSERT INTO USER_RECIPES (USER_ID, RECIPE_ID) VALUES (3, 4);
