# Testing  

1. [Validators](#Validators)
    1. [Exceptions](#Exceptions)
2. [Responsiveness](#Responsiveness)
    1. [Devices](#Devices)
    2. [Browsers](#Browsers)
3. [Functionality Tests](#Functionality-tests)
    1. [Note for the Assessor](#Note-for-the-assessor)

4. [Bugs](#bugs)
    1. [Solved Bugs](#Solved-bugs)
    2. [Unsolved Bugs](#Unsolved-bugs)

## Validators

- HTML was checked on [HTML Validator](https://validator.w3.org/).
- CSS was checked on [CSS Validator](http://csslint.net/).
- JavaScript was checked on [JS Hint Validator](https://jshint.com/).
- Python was checked on [PEP8 online check](http://pep8online.com/).

### Exceptions
Certain code which returns an error when passed through a validator have been left in because they fall under these categories:
- Code provided by libraries - in settings.py there is code that are too long which is how it was written when the django project was created.
- Code taken from the code institute example project - Unless I thought it broke clean code rules unintentionally I didn't change the code to follow the guidelines since I trust the course to provide clean code.
- Line too long where making a new line isn't possible - For python files certain lines shouldn't be broken i.e. split_filtered_products=all_products.filter(category__name__in=split_category)[start_point:end_point]
- HTML Templates extending the base: All templates, outside of the base, are missing the the header and !DOCTYPE so show an error on being passed through the validator. 

## Responsiveness 

### Devices
- Monitor _1920x1080_
- Macbook Pro 2015
- Windows 10 Laptop _1366x768_
- Ipad Pro 11"
- Iphone SE (2nd Generation)
- Xiaomi 9 Lite
- Samsung A8s

### Browsers
- Firefox
- Safari
- Chrome
- Edge

Since Internet Explorer will be deprecated later in the year, this site has not been optimised for Internet Explorer

## Functionality Tests

**Navbar Links**

- **Plan:** All links work and take the user to the correct page
- **Result:** This test passed.

**Registration Page**

- **Plan:** User can input a valid email format and will receive a verification email
- **Result:** This test passed.

**Login Page**

- **Plan:** After verifying their email, users can login and will be directed to the homepage.
- **Result:** This test passed.

**Reset Password**

- **Plan:** Users who have forgotten their passwords can reset their password with a confirmation email
- **Result:** This test has passed.

**Change Password**

- **Plan:** Logged in users can change their passwords from their profile page.
- **Result:** This test has passed.

**Workshop Button - When User is Logged In**

- **Plan:** User clicks the **_“Check our workshops”_** button and is directed to the workshops page.
- **Result:** This test has passed.

**Profile Page**

- **Plan:** Logged in users can view their profile, Non-logged in users will be redirected to login page.
- **Result:** This test has passed.

**Manage Email Addresses**

- **Plan:** Logged in users can add and remove multiple email addresses and change which email is their primary email.
- **Result:** This test has passed.

**Re-send verification Email**

- **Plan:** Logged in users can re-send verification emails.
- **Result:** This test has passed.

**Order History**

- **Plan:** Logged in users can view all of their past orders via the profile page (non-logged in users will need to save the confirmation email)
- **Result:** This test has passed.

**PLP to PDP**

- **Plan:** Clicking on a product image, product name or view product button takes the user to the appropriate product page.
- **Result:** This test has passed.

**Filtering**

- **Plan:** Users can filter products displayed by category
- **Result:** This test has passed.

**Sorting**

- **Plan:** Users can sort products displayed by name and price
- **Result:** This test has passed.

**Product Search**

- **Plan:** Users can use search bar to find specific products.
- **Result:** This test has passed.

**Add to Bag (PLP)**

- **Plan:** The add to bag button adds one unit to the bag and shows the full bag in a pop out message.
- **Result:** This test has passed.

**Add to Bag (PDP)**

- **Plan:** The add to bag button adds the value from the input field and shows the full bag in a pop out message
- **Result:** This test has passed.

**PDP to PLP**

- **Plan:** Users can return to the products page by click the “keep shopping” button
- **Result:** This test has passed.

**Contact Us Form**

- **Plan:** Users can submit a contact form which is stored on the site admin.
- **Result:** This test has passed.

**Bag Page**

- **Plan:** Users can view their full bag.
- **Result:** This test has passed.

**Return to Proucts Page**

- **Plan 1:** If users have nothing in their bag they will be told and provided a button to return to the products page
- **Result:** This test has passed.

**Edit Bag Items**

- **Plan 1:** IUsers can adjust quantity and remove items from their bag on the bag page.
- **Result:** This test has passed.

**Proceed to Checkout**

- **Plan 1:** Users can go to the checkout page by clicking the “proceed to checkout” button on the bag page.
- **Result:** This test has passed.

**Checkout**

- **Plan 1:** Users can fill out their delivery information and submit their order for confirmation through stripe.
- **Result:** This test has passed.

**Change Delivery Regions**

- **Plan 1:** When users change the country on the delivery information the grand total and delivery cost will change dynamically to show them the new price.
- **Result:** This test has passed.

**No Duplicate Orders**

- **Plan 1:** If the order fails to be checked and the user submits the form again, they will not be billed twice and the order does not appear twice in the site admin
- **Result:** This test has passed.

**Checkout Successful**

- **Plan 1:** On the order being processed successfully the user will be redirected to the checkout success page where they will be able to view their receipt/order. 
- **Result:** This test has passed.

**Checkout Successful to Checkout Page**

- **Plan 1:** If a user uses the back button on the checkout success page after just submitting a successful order they will be redirected to the products page.
- **Result:** This test has passed.

**Checkout Successful Return to Homepage**

- **Plan 1:** Return to homepage button takes the user back to the homepage
- **Result:** This test has passed.

**Scroll Transition**

- **Plan 1:** When users scroll the opacity on the background color for the navbar becomes solid and becomes transparent when user scrolls back up to the top
- **Result:** This test has passed.

**Edit Products - Superuser**

- **Plan 1:** Superusers can edit products from the products page
- **Result:** This test has passed.

**Add Products - Superuser**

- **Plan 1:** Superusers can add products from product management page.
- **Result:** This test has passed.

**Remove Products - Superuser**

- **Plan 1:** Superusers can remove products from the products page.
- **Result:** This test has passed.

### Note for the assessor


To test the CRUDs functionalities as a **normal user**:

| **Username** | **Password** |
| ------------ | ------------ |
| testuser     | tester232    |

To test the CRUDs functionalities as **superuser**:

| **Username**  | **Password**  |
| ------------- | ------------- |
| testsuperuser | supertester232|

To purchase a product, use the information below:

| Card Number      | MM/YY | CVC | ZIP Code  |
| ---------------- | ----- | --- | --------- |
| 4242424242424242 | 04/24 | 424 | 42424     |

## Bugs

### Solved bugs

- **Bug 1**

  - **Problem:** Screen was not scrolling even when content went below the viewport.
  - **Cause:** All of the content was sat inside the overlay div which had a height of 100% which
  - **Solution:** Moved all content out of the overlay div 

- **Bug 2**

  - **Problem:** Delivery cost stopped updating when users clicked on different countries.
  - **Cause:** I had added a “£” sign to the delivery cost and since I was trying to change the string to a number it was return “NaN”.
  - **Solution:** Added step to update delivery cost which removed the “£” from the string before converting the format. 

- **Bug 3**

  - **Problem:** The current bag value would display £4.00 when there was nothing in the basket.
  - **Cause:** The logic for the bag grand total was adding £4.00 if the sum of the items price didn’t meet the delivery threshold.
  - **Solution:** Added a condition to the template tag where if the value is 4 then the value wouldn’t display since the minimum order value would have to the product price + 4 or meet the delivery threshold. 

- **Bug 4**

  - **Problem:** Logo wasn’t loading after project was deployed to heroku.
  - **Cause:** the {{MEDIA_URL}} variable wasn’t populating properly.
  - **Solution:** Hard coded the url to point to the AWS S3 bucket. 

### Unsolved bugs

- Users can add more than 99 units of a product by typing it in.
- Forms on allauth templates are appearing squished horizontally - still trying to find on what screens/browsers on which this occurs.
- Pages using white backgrounds are not always covering the remaining viewport height. This bug has been partly fixed using the calc attribute with “vh” but has not yet been correctly applied for all instances.