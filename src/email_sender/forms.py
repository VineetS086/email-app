from django import forms

class EmailForm(forms.Form):

    from_addr       = forms.EmailField(label="From",
                        widget=forms.EmailInput(
                            attrs={

                                "class"         : "form-control",
                                "placeholder"   : "you@example.com",
                                
                            }
                        ))

    password        = forms.CharField(label="Password", 
                        widget=forms.PasswordInput(
                            attrs={

                                "class"         : "form-control",
                                "placeholder"   : "Password",
                                
                            }
                        ))

    to_addr         = forms.CharField(label="TO", 
                        widget=forms.TextInput(
                            attrs={

                                "class"         : "form-control",
                                "placeholder"   : "name@example.com",
                                
                            }
                        ))
                        
    cc_addr         = forms.CharField(label="CC", required=False,
                        widget=forms.TextInput(
                            attrs={

                                "class"         : "form-control",
                                "placeholder"   : "cc_name@example.com",
                                
                            }
                        ))
    
    bcc_addr        = forms.CharField(label="BCC", required=False, 
                        widget=forms.TextInput(
                            attrs={

                                "class"         : "form-control",
                                "placeholder"   : "bcc_name@example.com",
                                
                            }
                        ))
    
    subject         = forms.CharField(label="SUBJECT", required=False,
                        widget=forms.TextInput(
                            attrs={

                                "class"         : "form-control",
                                "placeholder"   : "Subject of the Email",
                                
                                
                            }
                        ))
    
    text            = forms.CharField(label="TEXT",
                        widget=forms.Textarea(
                            attrs={

                                "class"         : "form-control",
                                "placeholder"   : "Email Content",
                                
                            }
                        ))
    
    