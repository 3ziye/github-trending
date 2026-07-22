# Responsible disclosure report 2022-2025 - Oversecured found 176 vulnerabilities in Samsung preinstalled apps

Oversecured is a leading mobile security provider specializing in detecting vulnerabilities in Android and iOS apps. 

Our team at Oversecured shares global security values and strives to continuously improve our mobile app scanning technology to ensure its excellence.

In this article, we share 176 vulnerabilities that we discovered and worked with Samsung to fix throughout our collaboration, including detailed descriptions of 140 of them.

We at Oversecured are incredibly proud of our collaboration with Samsung in making mobile apps more secure. Our strong partnership with Samsung allows us to work together toward improving global mobile security. 

Also, our results demonstrate the capability of our scanner to handle most vulnerabilities where others may fall short. Let’s take a closer look at what we have achieved.

## Introduction

Samsung is a leading global electronics company making popular mobile devices based on Android. 
As a company with a wide range of products, it is unsurprising that they have a vast amount of software code to maintain. 

Samsung has one of the most competent cybersecurity teams in the industry, consistently working to improve its security measures. They have implemented various measures to ensure the safety of their users, including a [vulnerability disclosure program](https://security.samsungmobile.com/securityReporting.smsb) and regular security audits.

In 2021, Oversecured already conducted a [two-week research](https://blog.oversecured.com/Two-weeks-of-securing-Samsung-devices-Part-1/) on Samsung's system app security, which resulted in the discovery of 17 vulnerabilities. We were happy to help Samsung to identify and fix these vulnerabilities, ensuring that their products remain secure for their mobile device users.

Our research 2022-2025 uncovered risky vulnerabilities in Samsung's mobile apps, and we promptly reported them to Samsung's VDP team. We were impressed by Samsung's quick response and efficient handling of the vulnerabilities we reported. As a result, millions of Samsung users can rest assured that their devices are now as secure as those running on AOSP. More details about our research can be found in our [previous article](https://blog.oversecured.com/Discovering-vendor-specific-vulnerabilities-in-Android/).


## List of vulnerabilities

There is a list of vulnerabilities we have found through our research. All of these vulnerabilities are already fixed with our help.

The vulnerabilities are sorted by date of report and fix. When this article was published, Samsung had rewarded the Oversecured team **$163.475** and ranked first in their [security research ranking](https://security.samsungmobile.com/hallOfFameInfo.smsb).

We also selected some of the most exciting vulnerabilities and described them in [a separate article](https://blog.oversecured.com/) on the Oversecured blog.

| #   | App                         | Description                                                                                                                                                                                                                                                                                                                       | Reward |
| --- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 1   | Settings                    | [Intent redirection with system privilege](001.%20Settings%20%E2%80%94%20Intent%20redirection%20with%20system%20privilege)                                                                                                                                                                                                        | $4850  |
| 2   | FactoryCamera               | [Corruption of arbitrary files with system privilege](002.%20FactoryCamera%20%E2%80%94%20Corruption%20of%20arbitrary%20files%20with%20system%20privilege)                                                                                                                                                                         | $10310 |
| 3   | Galaxy Themes Service       | [Uninstalling arbitrary apps](003.%20Galaxy%20Themes%20Service%20%E2%80%94%20Uninstalling%20arbitrary%20apps)                                                                                                                                                                                                                     | $5580  |
| 4   | Galaxy Themes Service       | [Directory listing with system privilege](004.%20Galaxy%20Themes%20Service%20%E2%80%94%20Directory%20listing%20w